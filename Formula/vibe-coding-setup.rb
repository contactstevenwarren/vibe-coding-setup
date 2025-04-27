class VibeCodingSetup < Formula
  desc "Vibe Coding project setup script"
  homepage "https://github.com/contactstevenwarren/vibe-coding-setup"
  url "https://github.com/contactstevenwarren/vibe-coding-setup/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "2d6710498634b89def75b51cf1bacbb50406659cd3ca32020992114a87852188"
  license "MIT"

  depends_on "python@3"

  def install
    bin.install "vibe-coding-setup"
  end

  test do
    system "#{bin}/vibe-coding-setup", "--version"
  end
end 