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