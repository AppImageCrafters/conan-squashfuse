from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    command = "sudo apt-get -qq update && sudo apt-get -qq install -y libfuse-dev"
    remotes = [("https://api.bintray.com/conan/bincrafters/public-conan", "yes", "bincrafters")]
    builder = ConanMultiPackager(remotes=remotes, build_policy="outdated", docker_entry_script=command)
    builder.add_common_builds()
    builder.run()
