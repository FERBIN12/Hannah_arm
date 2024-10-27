from setuptools import find_packages, setup

package_name = 'py_service'

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
            'service = py_service.service_member_function:main',
            'client = py_service.client_member_function:main',
        ],
    },
)
