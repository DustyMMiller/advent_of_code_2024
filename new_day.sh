#!/bin/bash
cp -r template/ day$1
mv day$1/template.py day$1/day$1.py
touch day$1/example.txt
sed -i '' "s/day01/day$1/g" "day$1/day$1.py"
