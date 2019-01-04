$(document).ready(registerHandlers);

function registerHandlers()
{
    $("#qr").click(() => openPage("share"));
    $("#results").click(() => openPage("respond/results"));
    $("#close").click(() => openPageAction("close"));
    $("#delete").click(() => openPageAction("delete"));
    $("#create").click(() => openPageAction("create"));
}

function getSelectedPoll()
{
    return $("input[name=poll-radio]:checked").val();
}

function openPage(page)
{
    window.open("../" + page + "?id=" + getSelectedPoll(), "_blank");
}

function openPageAction(action)
{
    const $form = $('<form method="POST" action="action"><input type="hidden" name="type" value="' + action + '"></form>');
    $("body").append($form);
    $form.submit();
}