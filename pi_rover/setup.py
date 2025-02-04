from setuptools import setup
import os
from glob import glob


package_name = 'pi_rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'meshes'),glob('meshes/*')),
        (os.path.join('share', package_name,'launch'),glob('launch/*')),
        (os.path.join('share', package_name,'urdf'),glob('urdf/*')),
        (os.path.join('share', package_name,'worlds'),glob('worlds/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2',
    maintainer_email='messerschmidt.markus@web.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'qr_maze_solve_node= pi_rover.maze_race:main',
            'line_runner = pi_rover.line_runner:main'
        ],
    },
)
