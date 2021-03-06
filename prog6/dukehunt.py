#!/usr/bin/env python3

# Next line disables pylint warnings about bottle.request.params:
# pylint: disable=E1135,E1136

import bottle

        
@bottle.route('/<filename:path>')
def send_static(filename):
    if filename.endswith('.py'):
        return "You may not have that file."

    import os.path
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)    
    return bottle.static_file(filename, root=dir_path)

@bottle.route('/dukehunt')
def index():
    """Home page."""
    return TITLE_HTML

@bottle.route('/play')
def play():
    """Gameplay page request handler."""
    return GAME_HTML

TITLE_HTML = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>

<head>
    <title>Duke Hunt</title>
    <style type='text/css'>
        body {
            background: black;
            border: 100;
            color: white;
        }
    </style>
</head>

<body>
    <center>

        <img src='img/dukehunt.gif' />
        <br />
        <h3>How to Play</h3>
        <p>
            Click <b>Update World</b> to advance one turn. Vegetation does not move. Dukes (and decoys!) do move.
            Click on an on-screen entity to lose 5 turns <i>and</i> reveal it (if it is a duke), detonate it (if it is a
            decoy), or simply lose 5 turns (vegetation).
        </p>
        <hr />
        <h3>Credits:</h3>
        <ul>
            <li>2dogSound_tadaa1_3s_2013jan31_CC-BY-30-US.wav by rdholder shared under the Creative Commons Attribution license.</li>
            <li>freesound.org &mdash; other sound effects</li>
        </ul>
        <br />

        <form action='/play'>
            Number of Dukes <img src='img/duke.gif' />: <input type='text' name='numdukes' value='3' />
            <input type='submit' name='action' value='Start Game' />
        </form>

    </center>
    <audio src='sounds/EASTERN_SITAR_BRIGHT_1.mp3' autoplay='true' />
</body>

</html>
"""

GAME_HTML = """\
<!DOCTYPE html>
<html xmlns='http://www.w3.org/1999/xhtml'>

<head>
    <title>Duke Hunt</title>
    <style>
        a {
            color: yellow;
        }
        
        body {
            background-color: black;
            margin: 0;
            color: yellow;
        }
    </style>

</head>

<body>
    <center>
        <img src='img/dukehuntsmall.png' /> <br/>
        <table width='100%'>
            <tr>
                <td valign='bottom' align='right'><a href='?action=view'>Update World</a> </td>
                <td align='center' style='color:yellow'>
                    Turns: 0 | Undiscovered Dukes: 3
                </td>
                <td valign='bottom' align='left'><a href='/'>New Game</a></td>
            </tr>
        </table>
        <svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' width='1000px' height='500px'>
            
            <rect x='0' y='0' width='1000' height='500' fill='lightgreen' />

            <!-- TO DO: Replace the following "static" set of entities with 
                 those generated by the program --> 

            <a xlink:href="/play?action=click&amp;id=64481968">
                <image x="259" y="75" xlink:href="img/flower.gif" width="34" height="34" />
            </a>
            <a xlink:href="/play?action=click&amp;id=64480368">
                <image x="214" y="167" xlink:href="img/tree.gif" width="83" height="87" />
            </a>
            <a xlink:href="/play?action=click&amp;id=64483280">
                <image x="716" y="419" xlink:href="img/bush.gif" width="103" height="89" />
            </a>

        </svg>
        <br />
        <a href="/play?action=cheat" style='color: #222222'>Cheat Mode</a>
        <br />
    </center>
    <audio src='sounds/35631__reinsamba__crystal_glass.mp3' autoplay='true' />
</body>

</html>
"""

# Boilerplate bootstrapping logic for running as a standalone program
if __name__ == "__main__":
    import threading
    import time
    import webbrowser
    
    # Launch a background thread that will spawn a webbrowser in 1 second from thread start
    def wait_n_browse():
        time.sleep(1.0) # Race condition/hack, but likely to work in most cases...
        webbrowser.open("http://localhost:8080/dukehunt")

    threading.Thread(target=wait_n_browse, daemon=True).start()
    
    # Launch the BottlePy dev server 
    import wsgiref.simple_server
    wsgiref.simple_server.WSGIServer.allow_reuse_address = 0

    # Launch the BottlePy dev server on the main thread (runs until Ctrl-Brk)
    bottle.run(host="localhost", port=8080, debug=True)
