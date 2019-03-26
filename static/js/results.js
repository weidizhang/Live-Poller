$(document).ready(loadResultsBlock);

const refreshTime = 15; // in seconds
let timeLeft = refreshTime;
let updateInterval;

function intervalHandler()
{
    timeLeft--;
    $("#counter").text(timeLeft);

    if (timeLeft == 1)
        $("#seconds-plural").hide();
    else
        $("#seconds-plural").show();

    if (timeLeft <= 0)
    {
        clearInterval(updateInterval);       

        $("#counter-text").hide();
        $("#updating-text").show();
        loadResultsBlock();
    }
}

function restartInterval()
{
    timeLeft = refreshTime;
    $("#counter").text(timeLeft);
    $("#counter-text").show();
    $("#updating-text").hide();

    updateInterval = setInterval(intervalHandler, 1000);
}

function loadResultsBlock()
{
    $.ajax({
        type: "GET",
        url: ajaxUrl,
        success: (data) => {
            $("#ajax-block").html(data);

            if (!pollClosed)
                restartInterval();
            else
                $("#update-block").hide();
        },
        error: restartInterval
    });
}