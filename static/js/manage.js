$(document).ready(onReady);

let responseGroupHtml;

function onReady()
{
    registerHandlers();
    
    const $cloneGroup = $($("#original-response-group").get(0).outerHTML);
    $cloneGroup.removeAttr("id");
    responseGroupHtml = $cloneGroup.get(0).outerHTML;
}

function registerHandlers()
{
    $("#qr").click(() => openPage("share"));
    $("#results").click(() => openPage("respond/results"));
    $("#close").click(() => openPageAction("close"));
    $("#delete").click(() => openPageAction("delete"));
    $("#create").click(() => $("#create-modal").modal());

    $("#add-response-box").click(() => $("#response-group").append(responseGroupHtml));
    $(document).on("click", ".remove-response-input", function() { $(this).closest(".input-group").remove(); });
    $("#closes").flatpickr({
        altInput: true,
        altFormat: "F j, Y, h:i K",
        enableTime: true,
        dateFormat: "U",
        minDate: "today"        
    });
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
    if (!window.confirm("Are you sure you want to " + action + " this poll?"))
        return;

    const $form = $('<form method="POST" action="./">' +
        '<input type="hidden" name="id" value="' + getSelectedPoll() + '">' + 
        '<input type="hidden" name="action" value="' + action + '">' +
        '</form>');
    $("body").append($form);
    $form.submit();
}