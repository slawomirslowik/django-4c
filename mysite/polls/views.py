from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """
        <script>
            var counter = 0;
            function myFunction() {
                alert('Hello html world! Click counter: ' + counter);
                counter++;
            }
        </script>
        <div>
            <p>Hello, world. You're at the polls index.</p>
            <br>
            <button id='button1' style="background-color:red" onclick="myFunction()">Click me!</button>
        </div>
        """
        )
