{
  "targets": [
    {
      "cflags": [
        "-std=c++0x",
        "-Wall",
        "-g",
        "-Wextra"
      ],
      "include_dirs": ["/home/ec2-user/dsdriver/include"],
      "link_settings": {
        "libraries": [
          "-L/home/ec2-user/dsdriver/include",
          "-L/home/ec2-user/dsdriver/lib",

        ],
      },
      "target_name": "db2",
      "sources": [ "src/binding.cc", "src/connection.cc", "src/connection.hh" ]
    }
  ]
}

