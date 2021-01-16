FROM willfarrell/crontab

RUN apk add python3 cmd:pip3
RUN pip3 install statsd PyYAML boto3
COPY certificate_check.py /to the path that you want
COPY certificate_check_base_on_file.py /to the path that you want
COPY the file of the sites /the path that you want
ENV AWS_DEFAULT_REGION=<ur region>
RUN echo "0 */2 * * *   python3 /the file " >> /etc/crontabs/root
RUN echo "0 */2 * * *   python3 /the file " >> /etc/crontabs/root


CMD ["crond", "-f"]


*****
By that you can create a container that will run your scripts on cron (you can set the time that you want, you can had after the file option to get the logs as well).
*****
