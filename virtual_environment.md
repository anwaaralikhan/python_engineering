
# Virtual Environments

*   Individual projects to have isolated context for installing packages.
*   Always work inside a virutal environment.
    *   No global installs anymore
    *   Create a virtual env. for every project
*   Isolate project dependencies.
    *   No more conficts with other projects


# Install Virtual Environment Globally

*  python -m pip install virtualenv
*  virtualenv --version

# Create Virtual Environment in different/separate folders

*  For Windows
   *  Goto HOME_DIRECTORY
      *  Create folder virtualenvs
         *  mkdir virtualenvs
         *  cd virtualenvs
         *  virtualenv new_project
         *  virtualenvs
            *  new_project
               *  Separate Python Environment will be created with packages (pip, setup tools, wheels ...
               *  Dedicated python and pip will be installed here
            *  Setup Python 3 Specific enviornment
                  *  virtualenv -p python3 new_project_version3
                  *  new_project_version3 will be created
               
   
