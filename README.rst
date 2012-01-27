Hadoop and Hive Python Thrift Libs
**********************************

This is an eggified version of the hadoop and hive thrift python
libraries.

The libs are extracted from clouderas hadoop distribution and the
version of this package includes the upstream version of the hadoop
distribution.

========================
Building the Distribtion
========================

To build the distribution from the source tree, run the following::

 python bootstrap.py
 ./bin/buildout
 ./bin/build

The above commands download the hadoop and hive tarballs from the
cloudera distribution.
