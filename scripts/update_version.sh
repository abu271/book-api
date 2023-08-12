#!/bin/bash

# Read the current version from the version.txt file
current_version=$(cat version.txt)

# Prompt user for the version update type
echo "Current version: $current_version"
read -p "Enter version update type (major, minor, patch): " update_type

# Validate user input
if [[ "$update_type" != "major" && "$update_type" != "minor" && "$update_type" != "patch" ]]; then
    echo "Invalid update type. Please enter 'major', 'minor', or 'patch'."
    exit 1
fi

# Split the version into major, minor, and patch parts
IFS='.' read -ra version_parts <<< "$current_version"
major="${version_parts[0]}"
minor="${version_parts[1]}"
patch="${version_parts[2]}"

# Update the version based on the user input
if [[ "$update_type" == "major" ]]; then
    major=$((major + 1))
    minor=0
    patch=0
elif [[ "$update_type" == "minor" ]]; then
    minor=$((minor + 1))
    patch=0
elif [[ "$update_type" == "patch" ]]; then
    patch=$((patch + 1))
fi

# Write the updated version back to the version.txt file
updated_version="$major.$minor.$patch"
echo "$updated_version" > version.txt

echo "Version updated to $updated_version"
