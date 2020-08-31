# 此脚本可用于开发调试时应用代码的实时变更

cwd=$(pwd)

$cwd/docker_build_debug.sh
$cwd/docker-compose-up-dev.sh

