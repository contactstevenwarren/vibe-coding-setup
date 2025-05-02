class VibeCodingSetup < Formula
  desc "Vibe Coding project setup script"
  homepage "https://github.com/contactstevenwarren/vibe-coding-setup"
  url "https://github.com/contactstevenwarren/vibe-coding-setup/archive/refs/tags/v1.1.1.tar.gz"
  sha256 "41f7438a4dc43d0e87bb947e446492aeb57e9591a6769047816af73776d91f29"
  license "MIT"

  depends_on "python@3"

  def install
    bin.install "vibe-coding-setup"
  end

  test do
    system "#{bin}/vibe-coding-setup", "--version"
  end
end 