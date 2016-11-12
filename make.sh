#!/bin/bash

buildid -n
NAME="upsilon-reactor-`buildid -k tag`"

mkdir $NAME

mkdir -p $NAME/src/
cp -r src/*.py $NAME/src/

mkdir -p build/distributions/
zip -r "build/distributions/$NAME".zip $NAME

rm -rf $NAME
