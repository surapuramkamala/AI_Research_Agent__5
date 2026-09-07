import time


def retry_tool(
    function,
    *args,
    retries=3,
    delay=2,
    **kwargs
):
    """
    Retry a tool if it fails.
    """

    last_error = None

    for attempt in range(1, retries + 1):

        try:

            print(
                f"[RETRY] Attempt "
                f"{attempt}/{retries}"
            )

            result = function(
                *args,
                **kwargs
            )

            print(
                f"[RETRY] Attempt "
                f"{attempt} succeeded"
            )

            return {
                "success": True,
                "result": result,
                "attempt": attempt
            }

        except Exception as error:

            last_error = str(error)

            print(
                f"[RETRY] Attempt "
                f"{attempt} failed"
            )

            print(
                f"[RETRY] Error: "
                f"{last_error}"
            )

            if attempt < retries:

                print(
                    f"[RETRY] Waiting "
                    f"{delay} seconds..."
                )

                time.sleep(delay)

    return {
        "success": False,
        "error": last_error,
        "attempt": retries
    }