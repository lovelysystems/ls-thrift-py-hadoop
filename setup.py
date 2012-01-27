##############################################################################
#
# Copyright 2012 Lovely Systems GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
##############################################################################

import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description='\n'.join((
        read('README.rst'),
        read('CHANGES.txt'),
        ))

setup(
    name="ls-thrift-py-hadoop",
    version="1_cdh3u2",
    description="Hadoop and Hive Python Thrift Libs",
    url="https://github.com/lovelysystems/ls-thrift-py-hadoop",
    long_description=long_description,
    author = "Lovely Systems",
    author_email = "office@lovelysystems.com",
    license='Apache License, Version 2.0',
    keywords = "map reduce hive hadoop thrift",
    packages=find_packages('src/'),
    package_dir = {'':'src'},
    zip_safe = True,
    )
