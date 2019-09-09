# Copyright 2019 Louise Poubel
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

"""Launch Gazebo and RViz with Dolly and SimSlides."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    pkg_dolly_gazebo = get_package_share_directory('dolly_gazebo')
    pkg_rosconjp_2019 = get_package_share_directory('rosconjp_2019')

    # Dolly launch
    dolly = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_dolly_gazebo, 'launch', 'dolly.launch.py'),
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(pkg_rosconjp_2019, 'worlds', 'ROSConJP.world'), ''],
          description='SDF world file'),
        dolly
    ])
