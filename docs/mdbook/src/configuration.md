
Sugaroid saves some data to your PC. The path where `sugaroid` saves the data is `~/.config/sugaroid` on Linux and Mac OS, but on Windows it is in `C:\Users\<username>\AppData\sugaroid\`

This is the training database used my sugaroid to answer your questions. Particularly related to `sugaroid` brain, the files are `sugaroid.db` and `sugaroid.trainer.json`

* `sugaroid.db` : The Sugaroid bot uses `SQLite` to read data from a persistent database. Remove `sugaroid.db` will reset `sugaroid`'s brain, and a fresh database will be created  from scratch
* `sugaroid.trainer.json` : Is a JavaScript Object Notation file which stores trained responses in order to reset or retrain them whenever there is a necessity. This file may or may not be present in end user's systems and depends solely on the type of release `dev` or `stable`

There might also be additional files in the configuration directory. These are Audio files, In the case that the `audio` keyword is passed as an argument, it creates samples of audio files downloaded from the `Google` server to serve [TTS \(Text to Speech\)](https://cloud.google.com/text-to-speech) to the end user.