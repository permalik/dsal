{
  description = "dsal-python";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/release-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = false;
        };
        myPython = pkgs.python312;
        pythonWithPkgs = myPython.withPackages (pythonPkgs:
          with pythonPkgs; [
            pip
            virtualenvwrapper
            isort
            black
          ]);
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.alejandra
            pythonWithPkgs
            pkgs.readline
          ];

          shellHook = ''
            VENV=.venv
            if [ ! -d $VENV ]; then
                virtualenv $VENV
            fi
            source ./$VENV/bin/activate
            echo "Python virtual environment activated."

            # Source .bashrc
            . .bashrc
          '';
        };

        packages.default = pkgs.python3Packages.buildPythonApplication {
          pname = "dsal-python";
          version = "0.1.0";
          src = ./.;
          propagatedBuildInputs = [
            pkgs.python3Packages.isort
            pkgs.python3Packages.black
          ];
        };
      }
    );
}
