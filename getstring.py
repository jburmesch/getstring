

def get_string(prompt: str, max_words=0, min_words=1, max_chars=0, min_chars=1,
               options=[], case_sensitive_options=False) -> str:
    answer = input(prompt + "\n")

    if max_words != 0 and len(answer.split()) > max_words:
        print(f'Error: No more than {max_words} word(s) may be entered.')
        return get_string(
            prompt=prompt,
            max_words=max_words,
            min_words=min_words,
            max_chars=max_chars,
            min_chars=min_chars,
            options=options,
            case_sensitive_options=case_sensitive_options
        )

    if len(answer.split()) < min_words:
        print(f'Error: At least {min_words} word(s) must be entered.')
        return get_string(
            prompt=prompt,
            max_words=max_words,
            min_words=min_words,
            max_chars=max_chars,
            min_chars=min_chars,
            options=options,
            case_sensitive_options=case_sensitive_options
        )

    if max_chars > 0 and len(answer) > max_chars:
        print(f'Error: No more than {max_chars} character(s) may be entered.')
        return get_string(
            prompt=prompt,
            max_words=max_words,
            min_words=min_words,
            max_chars=max_chars,
            min_chars=min_chars,
            options=options,
            case_sensitive_options=case_sensitive_options
        )

    if len(answer) < min_chars:
        print(f'Error: At least {min_chars} character(s) must be entered.')
        return get_string(
            prompt=prompt,
            max_words=max_words,
            min_words=min_words,
            max_chars=max_chars,
            min_chars=min_chars,
            options=options,
            case_sensitive_options=case_sensitive_options
        )

    if len(options) > 0 and case_sensitive_options and (answer not in options):
        print(f'Error: Input options are: {options}. '
              + 'Options are case-sensitive.')
        return get_string(
            prompt=prompt,
            max_words=max_words,
            min_words=min_words,
            max_chars=max_chars,
            min_chars=min_chars,
            options=options,
            case_sensitive_options=case_sensitive_options
        )
    elif len(options) > 0 and check_non_case_options(answer, options):
        return get_string(
            prompt=prompt,
            max_words=max_words,
            min_words=min_words,
            max_chars=max_chars,
            min_chars=min_chars,
            options=options,
            case_sensitive_options=case_sensitive_options
        )

    return answer


def check_non_case_options(answer: str, options: list) -> None:
    upper_options = []
    for option in options:
        upper_options.append(option.upper())
    if answer.upper() not in upper_options:
        print(f'Error: Input options are: {options} '
                + '\n Options are not case-sensitive.')


if __name__ == "__main__":
    answer = get_string(
        'Please enter "This is a test."',
        options=['This is a test.'],
        case_sensitive_options=True
    )
    if answer == 'This is a test.':
        print("Success!")
