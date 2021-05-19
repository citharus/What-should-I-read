<p align="center"><img align="center" src="https://github.com/citharus/What-should-I-read/blob/master/assets/logo.png"/></p>
<h1 align="center">What should I read?</h1>

<p align="center"><b>What should I read?</b> is a Discord Bot which randomly gives a book from a predefined list.</p>
<br/><br/>

## Add the Bot to your Server
To add **What should I read?** to your discord server you have to accept the [invite link](https://discord.com/api/oauth2/authorize?client_id=753649712149692580&permissions=18432&scope=bot).  
To access the command overview send `&help` in the cannel or as a direct message to the bot.
<br/><br/>

## Commands
* `&help` Shows the command overview.  
* `&book <list>` Gives a random book from the `<list>`. You can see [available lists](https://github.com/citharus/What-should-I-read/blob/master/README.md/#Lists) here.
<br/><br/>

## Lists
* `times` The [Times top 100 best novels](https://en.wikipedia.org/wiki/Time%27s_List_of_the_100_Best_Novels).
* `guardian` The [Gurdians 100 best english novels](https://www.theguardian.com/books/2015/aug/17/the-100-best-novels-written-in-english-the-full-list).
<br/><br/>

## Roadmap
1. Add more lists
2. Add categorys
<br/><br/>

## Run the bot on your computer
To run the bot on your computer you first have to make a copy of the source code.
```bash 
  git clone https://github.com/citharus/What-should-I-read.git
```
For the bot to start you'll need a Discord Token. You get one if you create a [Discord Application](https://discord.com/developers/applications/).  
<img src="https://github.com/citharus/What-should-I-read/blob/master/assets/create_application.png"/>  
After creating the application navigate to the `Bot` tab in the menu to the right an click on the `Add Bot` button.   
<img src="https://github.com/citharus/What-should-I-read/blob/master/assets/menu.png"/>
<img src="https://github.com/citharus/What-should-I-read/blob/master/assets/bot.png"/>  
A conformation should pop up, you have to confirme it to proceed. After the conformation you are able to get the Discord Token.  
<img src="https://github.com/citharus/What-should-I-read/blob/master/assets/token.png"/>  
Copy and paste the Discord Token in the `TOKEN.txt` file. Make sure to remove the placeholder text.  

To finally run the Bot open a console and type  
for **Windows**
```bash
python3 pip install -r requirements.txt
python3 main.py
```
and for **Linux**
```bash
pip install -r requirements.txt
python main.py
```
<br/>

## License
[GNU General Public License v2.0](https://github.com/citharus/What-should-I-read/blob/master/LICENSE)
