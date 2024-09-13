<?php

declare(strict_types=1);

namespace Tests\Galeas\Api\UnitAndIntegration\Primitive\PrimitiveValidation\Email;

abstract class InvalidVerificationCodes
{
    /**
     * @return string[]
     */
    public static function listInvalidVerificationCodes(): array
    {
        return [
            '12345678901234567890', // too short (must be exactly 96 characters)
            '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345', // too short (must be exactly 96 characters)
            '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567', // too long (must be exactly 96 characters)
            '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', // too long (must be exactly 96 characters)
            '', // empty
            ' ', // spaces
            'a12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345', // leading letter
            '123456789012345678901234567890123456789a01234567890123456789012345678901234567890123456789012345', // letter in the middle
            '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345a', // letter at the end
            'A12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345', // uppercase leading letter
            '123456789012345678901234567890123456789A01234567890123456789012345678901234567890123456789012345', // uppercase letter in the middle
            '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345A', // uppercase letter at the end
            ' 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345', // leading space
            '123456789012345678901234567890123456789 01234567890123456789012345678901234567890123456789012345', // space in the middle
            '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345 ', // space at the end
            '!12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345', // leads with symbol
            '123456789012345678901234567890123456789!01234567890123456789012345678901234567890123456789012345', // symbol in the middle
            '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345!', // symbol at the end
        ];
    }
}
