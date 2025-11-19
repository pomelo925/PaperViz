#!/bin/bash

################################################################################
# PaperViz - Manim Animation Runner
# 
# This script provides an interactive interface to render Manim animations
# for various research papers.
#
# Usage:
#   ./run.sh [id]
#
# If ID is provided, directly render that paper's animation.
# If no ID is provided, show an interactive menu.
################################################################################

set -e

# Export DISPLAY for X11 forwarding
export DISPLAY=:0

# Set user permissions for Docker
export USER_ID=$(id -u)
export GROUP_ID=$(id -g)

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_FILE="$SCRIPT_DIR/docker/compose.cpu.yml"
PROJECT_NAME="paperviz"
CONTAINER_NAME="paperviz-manim"

# Paper definitions
declare -A PAPERS
PAPERS[1]="PLD: SELF-IMPROVING VISION-LANGUAGE-ACTION MODELS WITH DATA GENERATION VIA RESIDUAL RL"
PAPERS[2]="(Reserved for future paper)"
PAPERS[3]="(Reserved for future paper)"

declare -A PAPER_SCRIPTS
PAPER_SCRIPTS[1]="papers/1_pld/pld_scene.py"
PAPER_SCRIPTS[2]=""
PAPER_SCRIPTS[3]=""

declare -A PAPER_SCENES
PAPER_SCENES[1]="PLDComplete"
PAPER_SCENES[2]=""
PAPER_SCENES[3]=""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

################################################################################
# Functions
################################################################################

print_header() {
    echo ""
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                         PaperViz                               ║${NC}"
    echo -e "${BLUE}║              Manim Animation Toolkit for Papers                ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_menu() {
    echo -e "${GREEN}Select a paper to visualize:${NC}"
    echo ""
    for id in $(echo "${!PAPERS[@]}" | tr ' ' '\n' | sort -n); do
        echo -e "  ${YELLOW}[$id]${NC} ${PAPERS[$id]}"
    done
    echo ""
    echo -e "  ${YELLOW}[0]${NC} Exit"
    echo ""
}

render_animation() {
    local paper_id=$1
    local script_path="${PAPER_SCRIPTS[$paper_id]}"
    local scene_name="${PAPER_SCENES[$paper_id]}"
    
    if [ -z "$script_path" ] || [ -z "$scene_name" ]; then
        echo -e "${RED}Error: Paper ID $paper_id is not yet implemented.${NC}"
        return 1
    fi
    
    echo -e "${GREEN}Rendering animation for Paper ID: $paper_id${NC}"
    echo -e "${BLUE}Title: ${PAPERS[$paper_id]}${NC}"
    echo ""
    
    # Ensure Docker container is running
    echo "Starting Docker container..."
    docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" up -d manim
    
    # Wait for container to be ready
    sleep 2
    
    # Render the Manim scene
    echo ""
    echo -e "${GREEN}Rendering Manim scene: $scene_name${NC}"
    echo -e "${YELLOW}Quality: 1080p @ 144fps (Ultra High Quality)${NC}"
    echo -e "${YELLOW}This may take a few minutes...${NC}"
    echo ""
    
    docker exec -it "$CONTAINER_NAME" manim --resolution 1920,1080 --frame_rate 144 "$script_path" "$scene_name"
    
    local exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✓ Animation rendered successfully!${NC}"
        echo -e "${BLUE}Output saved to: workspace/media/${NC}"
        echo ""
    else
        echo ""
        echo -e "${RED}✗ Error rendering animation (exit code: $exit_code)${NC}"
        echo ""
        return 1
    fi
}

cleanup() {
    echo ""
    echo -e "${YELLOW}Stopping Docker container...${NC}"
    docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" down 2>/dev/null || true
    echo -e "${GREEN}Cleanup complete.${NC}"
}

################################################################################
# Main Script
################################################################################

# Trap cleanup on exit
trap cleanup EXIT

print_header

# Check if ID argument is provided
if [ $# -eq 1 ]; then
    PAPER_ID=$1
    
    # Validate ID
    if [ "$PAPER_ID" == "0" ]; then
        echo -e "${YELLOW}Exiting...${NC}"
        exit 0
    fi
    
    if [ -z "${PAPERS[$PAPER_ID]}" ]; then
        echo -e "${RED}Error: Invalid paper ID: $PAPER_ID${NC}"
        echo ""
        print_menu
        exit 1
    fi
    
    # Render the animation
    render_animation "$PAPER_ID"
    
elif [ $# -eq 0 ]; then
    # Interactive mode
    while true; do
        print_menu
        
        read -p "Enter paper ID: " PAPER_ID
        
        # Validate input
        if [ "$PAPER_ID" == "0" ]; then
            echo -e "${YELLOW}Exiting...${NC}"
            exit 0
        fi
        
        if [ -z "${PAPERS[$PAPER_ID]}" ]; then
            echo -e "${RED}Invalid selection. Please try again.${NC}"
            echo ""
            continue
        fi
        
        # Render the animation
        render_animation "$PAPER_ID"
        
        # Automatically return to menu after rendering
        echo ""
    done
else
    echo -e "${RED}Error: Invalid number of arguments.${NC}"
    echo ""
    echo "Usage: $0 [paper_id]"
    echo ""
    echo "Examples:"
    echo "  $0        # Interactive mode"
    echo "  $0 1      # Render Paper ID 1"
    echo ""
    exit 1
fi

echo ""
echo -e "${GREEN}Done!${NC}"
