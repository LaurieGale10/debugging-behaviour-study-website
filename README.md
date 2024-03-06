# *Investigating the Debugging Behaviour and Attitudes of KS3 Students* Study Website

A single page application used to host the programming exercises for the study ["Investigating the Attitudes and Emotions of KS3 Students"](https://dl.acm.org/doi/10.1145/3610969.3611120) and Investigating the Debugging Behaviour of Lower Secondary Students (not yet published) in early 2023. Developed using vanilla JavaScript (embedding the [Ada CS Code Editor](https://github.com/isaacphysics/isaac-code-editor)), HTML, and CSS, using a Flask app to serve a Postgresql database (not included in this repo).

## Installation

1. Before running, make sure you have an up to date version of [Python](https://www.python.org/downloads/).
2. To run the project, simply run `python3 -m http.server` in the `website` folder (`cd website`) and then visit http://localhost:8000 to view the website.

## Additional Info

The `exercises` contains the original debugging exercises as they appeared to the students, as well as corrected solutions.

### Log Data Format:
For those interested in analysing programming log data, the format of this data is described below and collected using the Ada code editor's logging. When a student runs the code, the following entry is added to a JSON of logs:

```
{
    (optional) "error": {
        "error: string //The error message thrown by the program, only present in a log if "compiled" is false
    },
    "compiled": boolean, //Whether the program successfully ran or not. Will be false if the program contains syntax or runtime errors
    "snapshot": string, //The program at the time of running, expressed as a string
    "timestamp": int //The time the program was ran at
}
```

Every keystroke made inside the code editor was also logged but not used for analysis.