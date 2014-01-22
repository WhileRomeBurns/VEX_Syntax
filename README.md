# VEX Syntax

A [Sublime Text][3] package for Sidefx Software's VEX language which is used in the procedural visual effects software Houdini. With the Monokai color scheme selected:

<p align="center">
  <img src="http://shawnlipowski.com/git/vex_tmlanguage_screenshot.png" alt="VEX Syntax Markup Example"/>
</p>

### Installation

#### [Package Control][2]

Open the Command Palette (Shift-Cmd-P in OS X, Shift-Ctrl-P in Linux/Windows).
Select "Package Control: Install Package". Find and install VEX Syntax.

Package Control will automatically keep VEX Syntax up to date.

#### Manual Installation

First you must locate the Sublime Text [packages folder][1], then:

Manual installation via git:

    cd /path/to/sublime/packages/folder
    git clone https://github.com/WhileRomeBurns/VEX_Syntax VEX_Syntax

Manual installation without git:

    cd /path/to/sublime/packages/folder
    curl -L https://github.com/WhileRomeBurns/VEX_Syntax/tarball/master | tar xf -

### Contributing

You can send pull requests via GitHub. Do *not* edit the `VEX.tmLanguage` file directly. Edit the `VEX.JSON-tmLanguage` file instead and build the `.tmLanguage` file
from it using the _JSON to Property List_ build tool in
[AAAPackageDev][4].

### License (MIT)

**Copyright © 2014 Shawn Lipowski**

```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

[1]: http://docs.sublimetext.info/en/latest/basic_concepts.html#the-packages-directory
[2]: http://wbond.net/sublime_packages/package_control
[3]: http://www.sublimetext.com/
[4]: https://github.com/SublimeText/AAAPackageDev
