from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    install_deps_script = "sudo apt-get -qq update && sudo apt-get -qq install -y libfuse-dev"
    builder = ConanMultiPackager(docker_entry_script=install_deps_script)
    builder.add_common_builds()
    builder.run()
