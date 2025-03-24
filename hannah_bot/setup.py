from setuptools import find_packages, setup

package_name = 'hannah_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['tests_require']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kanja-koduki',
    maintainer_email='fjferbin@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_pub = hannah_bot.simple_publisher:main',
            'simple_sub = hannah_bot.simple_subscriber:main',
            'simple_parm = hannah_bot.simple_parameter:main',
            'simple_service_server = hannah_bot.simple_service_server:main',
            'simple_action_server = hannah_bot.simple_action_server:main',
            'simple_action_client = hannah_bot.simple_action_client:main',
        ],
    },
)
