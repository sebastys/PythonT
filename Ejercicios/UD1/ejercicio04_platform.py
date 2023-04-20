import platform

print(platform.platform())#Windows-10-10.0.19044-SP0
#En otro ordenador sale: Linux-5.10.162+-x86_64-with-glibc2.35
print(platform.platform(aliased=True))#Windows-10-10.0.19044-SP0
print(platform.platform(terse=True))#Windows-10
print(platform.machine())#AMD64
print(platform.processor())#Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
print(platform.system())#Windows
print(platform.version())#10.0.19044
print(platform.python_implementation())#CPython
print(platform.python_version_tuple())#('3', '11', '3') Tupla con los tres valores de la versión