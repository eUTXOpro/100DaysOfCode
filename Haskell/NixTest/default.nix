# default.nix
{ pkgs ? import <nixpkgs> {}, haskellPackages ? pkgs.haskellPackages }:
haskellPackages.ghcWithPackages (pkgs: with pkgs; [random])