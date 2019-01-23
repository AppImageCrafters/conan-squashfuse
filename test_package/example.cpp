#include <iostream>
extern "C" {
#include <squashfuse.h>
}


int main() {
    sqfs fd;
    int major, minor;
    sqfs_version(&fd, &major, &minor);
    std::cout << "SQFS Version: " << major << "." << minor << std::endl;
}
