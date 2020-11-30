# Memory

The Sugaroid bot has been designed to provide an acceptable answer and the author had been focusing on refining the response by the bot more and more better. However this has resulted in bad PEP practices and disallocated memory modules.

| Time | Memory \(KB\) | Memory \(MB\) |
| :--- | :--- | :--- |
| Initial Loading | 83500 KB | 83.5 MB |
| Pause after loading | 173800 KB | 173.8 MB |
| First Question \(Hello\) | 266500 KB | 266.5 MB |
| Second Question \(Hey\) | 287500 KB | 287.5 MB |
| Third Question \(Emotion\) | 289500 KB | 289.5 MB |
| Fourth Question \(Emotion\) | 289950 KB | 290 MB |

This is because, a lot of unnecessary objects have been created in the memory. This should be removed before the release of `sugaroid` version 1.0
