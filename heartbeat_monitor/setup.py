from setuptools import setup

package_name = 'heartbeat_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wheeltec',
    maintainer_email='wheeltec@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['heartbeat_publisher = heartbeat_monitor.heartbeat_publisher:main',
            'heartbeat_monitor = heartbeat_monitor.heartbeat_monitor:main',
        ],
    },
)
