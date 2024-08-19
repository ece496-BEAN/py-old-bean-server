{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs; [ 
    git # Source code versioning
    zellij # A better tmux (terminal multiplexer)
    atuin # Command history, to use it with fish, follow this: https://docs.atuin.sh/guide/installation/#installing-the-shell-plugin
    helix # A modal editor, similar to vim but different
    fish # A better shell than bash
    toybox # Unix command line utilities like which, clear
    less # file pager
    curl # Transferring files
  
    # python configured below
  ];

  languages.python = {
    enable = true;
    version = "3.12.4";
    venv.enable = true;
    venv.requirements = ''
      python-lsp-server

      mypy
      djangorestframework-stubs[compatible-mypy]

      pydantic
      beartype
      ruff

      django
      djangorestframework
    '';
  };

  pre-commit.hooks = {
    commitizen.enable = true;
  };

  
  enterShell = ''
  '';
}
