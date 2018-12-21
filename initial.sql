CREATE TABLE IF NOT EXISTS `polls` (
    `ID` TEXT,
    `Question` TEXT,
    `Created` INTEGER,
    `Closes` INTEGER,
    `Choices` TEXT,
    `NumChoices` INTEGER
);

CREATE TABLE IF NOT EXISTS `responses` (
    `PollID` TEXT,
    `Responses` TEXT
);