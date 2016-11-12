#!/bin/bash

mkdir -p pkg

buildid -n
NAME="upsilon-reactor-`buildid -k tag`"

mkdir $NAME

mkdir -p $NAME/src/
cp -r src/*.py $NAME/src/

zip -r "pkg/$NAME".zip $NAME

rm -rf $NAME
