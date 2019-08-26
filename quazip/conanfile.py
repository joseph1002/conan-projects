from conans import ConanFile, CMake, tools


class Quazip5Conan(ConanFile):
    name = "quazip"
    version = "0.8.1"
    license = "MIT"
    url = "https://github.com/stachenov/quazip.git"
    description = "quazip conan file"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    source_tgz = "https://github.com/stachenov/quazip/archive/v{}.tar.gz".format(version)

    def source(self):
        # self.run("git clone https://github.com/stachenov/quazip.git")
        tools.download(self.source_tgz, "quazip.tar.gz")
        tools.unzip("quazip.tar.gz")

    def _configure_cmake(self):
        cmake = CMake(self)
        # cmake.configure(source_folder="quazip")
        cmake.configure(source_folder="quazip-{}".format(self.version))
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    # def package(self):
    #     self.copy("*.h", dst="include", src="libquazip5")
    #     self.copy("*libquazip5.lib", dst="lib", keep_path=False)
    #     self.copy("*.dll", dst="bin", keep_path=False)
    #     self.copy("*.so", dst="lib", keep_path=False)
    #     self.copy("*.dylib", dst="lib", keep_path=False)
    #     self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["quazip5"]