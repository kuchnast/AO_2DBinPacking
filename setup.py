import setuptools


setuptools.setup(
    name="bin_packing_2d",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "argparse ~= 1.4",
        "pandas-stubs",
        "pandas",
        "types-tabulate",
        "tabulate",
    ],
    entry_points={'console_scripts': ['bin_packing_2d = main:main',
                                      'generate_input_data = data_operations.generate_input_data:generate_input_data']}
)
