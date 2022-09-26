
# aws conection.
def aws_client(aws_service, *args, **kwargs):
    def wrapper(function):
        try:
            if not aws_service:
                raise Exception("The parameter aws_service don't can be None!")

            aws_client = get_aws_client(aws_service=aws_service)
        except Exception as error:
            return error
        return function(*args, **kwargs, aws_client=aws_client)

    return wrapper


@aws_client(aws_service='sqs')
def function_aws_client(aws_client=None):
    return


# redis instance.


def get_redis_instance(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=settings.REDIS_DECODE_RESPONSES,
    token=settings.REDIS_TOKEN,
):
    if not bool(token):
        _redis = redis.Redis(
            host=host, port=port, decode_responses=decode_responses,
        )
    else:
        _redis = redis.StrictRedis(
            host=host,
            port=port,
            password=token,
            decode_responses=decode_responses,
            ssl=True,
        )
    try:
        _redis.client()
    except redis.ConnectionError:
        _redis = redis.Redis(
            host=host.replace('redis://', ''),
            port=port,
            decode_responses=decode_responses,
        )
        pass

    return _redis


def redis_instance(function):
    def wrapper(*args, **kwargs):
        redis_instance = get_redis_instance()
        return function(*args, **kwargs, redis_instance=redis_instance)

    return wrapper

@redis_instance
    def test_grouper_scenario_1(redis_instance=None):
        return