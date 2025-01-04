#!/bin/bash
curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain nightly -y
echo 'source $HOME/.cargo/env' >> $HOME/.bashrc
export PATH="${HOME}/.cargo/bin:${PATH}"