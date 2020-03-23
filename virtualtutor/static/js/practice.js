import { questions,questions1,questions2,questions3,questions4,questions5 } from './questions.js'
import { difficultylevel } from './assessment.js'

(function () {
    var questionCounter = 0; //Tracks question number
    var selections = []; //Array containing user choices
    var currQuestionsArr = questions;
    var quiz = $('#quiz'); //Quiz div object
    var calcResults = 0;
    var numCorrect = 0;



    // Display initial question
    displayNext();

    // Click handler for the 'next' button
    $('#next').on('click', function (e) {
        e.preventDefault();

        // Suspend click listener during fade animation
        if (quiz.is(':animated')) {
            return false;
        }
        choose();

        // If no user selection, progress is stopped
        if (isNaN(selections[questionCounter])) {
            alert('Please make a selection!');
        } else {
            questionCounter++;
            displayNext();
        }
    });

    // Click handler for the 'prev' button
    $('#prev').on('click', function (e) {
        e.preventDefault();

        if (quiz.is(':animated')) {
            return false;
        }
        choose();
        questionCounter--;
        displayNext();
    });

    // Click handler for the 'Start Over' button
    $('#start').on('click', function (e) {
        e.preventDefault();

        if (quiz.is(':animated')) {
            return false;
        }
        questionCounter = 0;
        selections = [];
        displayNext();
        $('#start').hide();
    });

    // Animates buttons on hover
    $('.button').on('mouseenter', function () {
        $(this).addClass('active');
    });
    $('.button').on('mouseleave', function () {
        $(this).removeClass('active');
    });

    // Creates and returns the div that contains the questions and
    // the answer selections
    function createQuestionElement(index) {
        var qElement = $('<div>', {
            id: 'question'
        });

        var header = $('<h2>Question ' + (index + 1) + '</h2>');
        qElement.append(header);

        var image = $('<img>', {
            src: currQuestionsArr[index].image,
            width: "450",
            height: "500"
        });
        qElement.append(image);

        var question = $('<p>').append(currQuestionsArr[index].question);
        qElement.append(question);

        var radioButtons = createRadios(index);
        qElement.append(radioButtons);

        return qElement;
    }

    // Creates a list of the answer choices as radio inputs
    function createRadios(index) {
        var radioList = $('<ul>');
        var item;
        var input = '';
        for (var i = 0; i < currQuestionsArr[index].choices.length; i++) {
            item = $('<li>');
            input = '<input type="radio" name="answer" value=' + i + ' />';
            input += ' ' + currQuestionsArr[index].choices[i];
            item.append(input);
            radioList.append(item);
        }
        return radioList;
    }

    // Reads the user selection and pushes the value to an array
    function choose() {
        selections[questionCounter] = +$('input[name="answer"]:checked').val();
    }

    // Displays next requested element
    function displayNext() {
        quiz.fadeOut(function () {
            $('#question').remove();

            if (questionCounter < currQuestionsArr.length) {
                var nextQuestion = createQuestionElement(questionCounter);
                quiz.append(nextQuestion).fadeIn();
                if (!(isNaN(selections[questionCounter]))) {
                    $('input[value=' + selections[questionCounter] + ']').prop('checked', true);
                }

                // Controls display of 'prev' button
                if (questionCounter === 1) {
                    $('#prev').show();
                } else if (questionCounter === 0) {

                    $('#prev').hide();
                    $('#next').show();
                }
            } else {
                var scoreElem = displayScore();
                quiz.append(scoreElem).fadeIn();
                $('#next').hide();
                $('#prev').hide();
                $('#start').show();
                numCorrect = 0;
            }
        });
    }

    // Computes score and returns a paragraph element to be displayed
    function displayScore() {
        var score = $('<p>', {id: 'question'});

        for (var i = 0; i < selections.length; i++) {
            if (selections[i] === currQuestionsArr[i].correctAnswer) {
                numCorrect++;
            }
        }
        score.append('Your score is ' + numCorrect + ' questions out of ' +
            currQuestionsArr.length);

        $.getJSON('/calc', {
        num: numCorrect
      },
        function(data) {
            $("#result").text(data.result);
            calcResults = data.result;
            if (calcResults > 70 && currQuestionsArr == questions){
                currQuestionsArr = questions1;
            }
            else if (calcResults > 70 && currQuestionsArr == questions1){
                currQuestionsArr = questions2;
            }
        });

        return score;
    }




     //$('#calculate').on('click', function(e) {
     //   e.preventDefault();
     //   $.getJSON('/calc', {
     //   num: numCorrect
     // },
     //   function(data) {
      //      $("#aria-valuenow").text(data.result);
      //  });
    //});
})();


