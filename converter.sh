#!/bin/bash
# Convert existing git repositories in data_lake/ to proper submodules

set -e  # exit on error

base_dir="data_lake"
backup_root="/tmp/submodule-backups"  # temporary storage for existing repos

mkdir -p "$backup_root"

# Loop over every item in data_lake
for dir in "$base_dir"/*/ ; do
    # Remove trailing slash
    dir=${dir%/}

    # Check if it's a git repository
    if [ ! -d "$dir/.git" ] && [ ! -f "$dir/.git" ]; then
        echo "Skipping $dir – not a git repository"
        continue
    fi

    echo "Processing $dir ..."

    # Get remote origin URL
    url=$(git -C "$dir" remote get-url origin 2>/dev/null || true)
    if [ -z "$url" ]; then
        echo "  No remote 'origin' found, skipping."
        continue
    fi

    # Get current commit
    commit=$(git -C "$dir" rev-parse HEAD)

    # Create a unique backup location
    backup_dir="$backup_root/$(basename "$dir")-$(date +%s)"
    echo "  Moving to backup: $backup_dir"
    mv "$dir" "$backup_dir"

    # Add submodule using the backup as reference (no network download)
    echo "  Adding submodule from $url"
    git submodule add --reference "$backup_dir" "$url" "$dir"

    # Reset to the exact commit we had (optional – comment out if not needed)
    echo "  Resetting to $commit"
    git -C "$dir" reset --hard "$commit"

    # Clean up backup
    rm -rf "$backup_dir"
    echo "  Done."
done

echo "All done. Check 'git status' and commit the changes."
