ARG USER=django

ARG PYTHON_VERSION=3.12-slim
ARG BUILD_ENVIRONMENT=local
ARG GROUP=${USER}
ARG HOME=/home/${USER}
ARG APP_HOME=${HOME}/app

########## BUILD STAGE ##########

FROM python:${PYTHON_VERSION} AS python

FROM python AS python-build-stage
ARG BUILD_ENVIRONMENT

RUN apt-get update && apt-get install --no-install-recommends -y \
build-essential \
libpq-dev \
curl 

WORKDIR ${APP_HOME}

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt 

########## RUN STAGE ##########

FROM python AS python-run-stage
ARG BUILD_ENVIRONMENT
ARG APP_HOME
ARG USER
ARG GROUP

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}
ENV USER ${USER}
ENV GROUP ${GROUP}

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    curl \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* 

RUN addgroup --system ${USER} && \
    adduser --system --ingroup ${USER} ${USER} 

RUN mkdir -p ${APP_HOME}/staticfiles && \
    chown ${USER}:${USER} ${APP_HOME}/staticfiles && \
    chmod 775 ${APP_HOME}/staticfiles

RUN mkdir -p ${APP_HOME}/media && \
    chown ${USER}:${USER} ${APP_HOME}/media && \
    chmod 775 ${APP_HOME}/media

WORKDIR  ${APP_HOME}

COPY ./src  ${APP_HOME}

COPY  --from=python-build-stage /usr/src/app/wheels /wheels/
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY --chown=${USER}:${USER}  ./docker/local/django/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=${USER}:${USER}  ./docker/local/django/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=${USER}:${USER}  ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY --chown=${USER}:${USER}  ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

COPY --chown=${USER}:${USER}  ./docker/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY --chown=${USER}:${USER}  ./docker/local/django/celery/beat/entrypoint /entrypoint-celerybeat
RUN sed -i 's/\r$//g' /entrypoint-celerybeat
RUN chmod +x /entrypoint-celerybeat

COPY --chown=${USER}:${USER} . ${APP_HOME}
RUN chown ${USER}:${USER} ${APP_HOME}

USER ${USER}

ENTRYPOINT [ "/entrypoint" ]