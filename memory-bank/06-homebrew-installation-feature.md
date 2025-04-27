# Homebrew Installation Feature Implementation

**Version:** 1.0  
**Date:** 2024-07-29

## Overview

This document outlines the implementation of Homebrew installation support for the "Vibe Coding Project Setup Script". This will allow users to easily install the script via Homebrew on macOS and Linux systems.

## Requirements

1. The script must be installable via Homebrew
2. Installation should create a globally accessible command
3. The implementation must follow Homebrew's best practices
4. Documentation should be updated to include installation instructions

## Implementation Steps

### 1. Package the Python Script

1. Rename the main script to `vibe-coding-setup` (without .py extension)
2. Add shebang line at the top of the script: `#!/usr/bin/env python3`
3. Make the script executable: `chmod +x vibe-coding-setup`
4. Test the script can run directly: `./vibe-coding-setup`

### 2. Create a Homebrew Formula

1. Create a new directory for the formula: `mkdir -p Formula`
2. Create a formula file in the directory: `Formula/vibe-coding-setup.rb`
3. Add the following content to the formula file:

```ruby
class VibeCodingSetup < Formula
  desc "Vibe Coding project setup script"
  homepage "https://github.com/contactstevenwarren/vibe-coding-setup"
  url "https://github.com/contactstevenwarren/vibe-coding-setup/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "[SHA256 hash of the tar.gz file]"
  license "MIT"

  depends_on "python@3"

  def install
    bin.install "vibe-coding-setup"
  end

  test do
    system "#{bin}/vibe-coding-setup", "--version"
  end
end
```

### 3. Set Up Version Check in Script

1. Add version command-line option to the script
2. Implement basic argument parsing:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Vibe Coding Project Setup Script")
    parser.add_argument("--version", action="store_true", help="Print version information")
    args = parser.parse_args()
    
    if args.version:
        print("Vibe Coding Setup v1.0.0")
        return
    
    # Existing script logic...
```

### 4. Create GitHub Repository

1. Create a new GitHub repository named "vibe-coding-setup"
2. Add LICENSE.md file with MIT license
3. Create a comprehensive README.md with usage instructions
4. Add all code files to the repository
5. Create a v1.0.0 tag and release

### 5. Create Homebrew Tap Repository

1. Create a new GitHub repository named "homebrew-vibe-coding"
2. Add the Formula directory with the formula file
3. Update the URL and SHA256 in the formula to match the actual release

### 6. Generate SHA256 Hash

1. After creating the GitHub release, download the tarball
2. Generate the SHA256 hash using the following command:
   ```bash
   shasum -a 256 vibe-coding-setup-1.0.0.tar.gz
   ```
3. Update the formula with the generated hash

### 7. Test Installation

1. Run `brew tap contactstevenwarren/vibe-coding`
2. Run `brew install vibe-coding-setup`
3. Test that `vibe-coding-setup` command works from any directory

## Installation Instructions for Users

To install the Vibe Coding Setup script via Homebrew:

```bash
# Add the tap repository
brew tap contactstevenwarren/vibe-coding

# Install the script
brew install vibe-coding-setup

# Verify installation
vibe-coding-setup --version
```

## Update Process for Maintainers

When releasing a new version:

1. Update version number in the script
2. Create a new tag and release on GitHub
3. Generate the SHA256 hash for the new release tarball
4. Update the formula's URL and SHA256 in the tap repository
5. Users can update with `brew upgrade vibe-coding-setup`

## Integration with Existing Implementation Plan

Add this as an additional phase to the Implementation Plan:

**Phase 5: Homebrew Installation Support**

11. **Step 11: Package Script for Homebrew**
    * **Task:** Add version flag, shebang line, and make script executable.
    * **Test:** Run `./vibe-coding-setup --version` and verify it prints the version.

12. **Step 12: Create GitHub Repository**
    * **Task:** Set up GitHub repository with MIT license, README, and code.
    * **Test:** Clone the repository and verify all files are included.

13. **Step 13: Create Homebrew Formula**
    * **Task:** Create a tap repository with the formula, including SHA256 hash.
    * **Test:** Install via Homebrew and verify the command works globally. 