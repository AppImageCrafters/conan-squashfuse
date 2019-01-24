from conans import ConanFile, AutoToolsBuildEnvironment, tools


class SquashfuseConan(ConanFile):
    name = "squashfuse"
    version = "0.1.103"
    license = "2-clause BSD"
    author = "Alexis Lopez Zubieta <contact@azubieta.net>"
    url = "https://github.com/azubieta/conan-squashfuse.git"
    description = "Squashfuse with patches for using it as a library in libappimage"
    topics = ("squashfs",)
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "patches/*"
    build_requires = ["lzma/5.2.4@bincrafters/stable", "fuse/2.9.9@azubieta/stable"]

    def source(self):
        git = tools.Git(folder="squashfuse.git")
        git.clone("https://github.com/vasi/squashfuse.git")
        git.checkout("1f98030")

        # Apply Patches
        self.run("cd squashfuse.git && patch -p1 < ../patches/squashfuse.patch")
        self.run("cd squashfuse.git && patch -p1 < ../patches/squashfuse_dlopen.patch")
        self.run("cp patches/squashfuse_dlopen.* squashfuse.git")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.fpic = True
        env_build_vars = autotools.vars
        self.run("cd squashfuse.git && ./autogen.sh")

        lzma_libs_dir = self.deps_cpp_info["lzma"].lib_paths[0];
        autotools.configure(configure_dir="squashfuse.git", vars=env_build_vars,
                            args=["--disable-demo", "--disable-high-level", "--without-lzo", "--without-lz4",
                                  "--with-xz=%s" % lzma_libs_dir])

        # https://github.com/vasi/squashfuse/issues/12
        self.run("cd squashfuse.git && sed -i \"/PKG_CHECK_MODULES.*/,/,:./d\" configure")

        # off_t's size might differ, see https://stackoverflow.com/a/9073762
        self.run("cd squashfuse.git && sed -i \"s/typedef off_t sqfs_off_t/typedef int64_t sqfs_off_t/g\" common.h")

        autotools.make(vars=env_build_vars)
        autotools.install(vars=env_build_vars)

    def package(self):
        self.copy("*.h", dst="include", src="squashfuse.git")
        self.copy("config.h", dst="include", src=".")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["squashfuse", "lzma", "z"]
