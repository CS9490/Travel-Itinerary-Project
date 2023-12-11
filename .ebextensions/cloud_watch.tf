resource "aws_cloudwatch_log_group" "flaskbb_app" {
  name              = "flaskbb_app"
  retention_in_days = 3
}

# CoRise TODO: create a new dashboard
resource "aws_cloudwatch_dashboard" "flaskbb_main" {
  dashboard_name = "flaskbb_main"

  dashboard_body = jsonencode(
    {
      "widgets" : [
        {
          "height" : 6,
          "width" : 6,
          "y" : 0,
          "x" : 0,
          "type" : "metric",
          "properties" : {
            "view" : "timeSeries",
            "stacked" : false,
            "metrics" : [
              ["flaskbb_app", "$auth/register_visitor_count"],
              ["flaskbb_app", "$forum/index_visitor_count"]
            ],
            "region" : "us-east-1",
            "start" : "-PT1H",
            "end" : "P0D",
            "title" : "Visitor Counts"
          }
        },
        {
          "type" : "log",
          "x" : 0,
          "y" : 6,
          "width" : 24,
          "height" : 6,
          "properties" : {
            "query" : "SOURCE 'flaskbb_app' | fields @timestamp, @message, @logStream, @log\n| sort @timestamp desc\n| limit 20",
            "region" : "us-east-1",
            "stacked" : false,
            "view" : "table"
          }
        },
        {
          "type" : "metric",
          "x" : 6,
          "y" : 0,
          "width" : 6,
          "height" : 6,
          "properties" : {
            "view" : "timeSeries",
            "stacked" : true,
            "metrics" : [
              ["AWS/ElasticBeanstalk", "ApplicationRequestsTotal", "EnvironmentName", "flaskbb-environment", { "region" : "us-east-1" }],
              ["AWS/ElasticBeanstalk", "ApplicationRequests2xx", "EnvironmentName", "flaskbb-environment", { "region" : "us-east-1" }],
              ["AWS/ElasticBeanstalk", "ApplicationRequests3xx", "EnvironmentName", "flaskbb-environment", { "region" : "us-east-1" }],
              ["AWS/ElasticBeanstalk", "ApplicationRequests4xx", "EnvironmentName", "flaskbb-environment", { "region" : "us-east-1" }],
              ["AWS/ElasticBeanstalk", "ApplicationRequests5xx", "EnvironmentName", "flaskbb-environment", { "region" : "us-east-1" }]
            ],
            "region" : "us-east-1",
            "period" : 300,
            "title" : "ApplicationRequests"
          }
        },
        {
          "type" : "metric",
          "x" : 12,
          "y" : 0,
          "width" : 6,
          "height" : 6,
          "properties" : {
            "metrics" : [
              ["AWS/ElasticBeanstalk", "ApplicationLatencyP90", "EnvironmentName", "flaskbb-environment"],
              [".", "ApplicationLatencyP99", ".", "."],
              [".", "ApplicationLatencyP99.9", ".", "."]
            ],
            "view" : "timeSeries",
            "stacked" : false,
            "region" : "us-east-1",
            "stat" : "Maximum",
            "period" : 300,
            "title" : "Application Latency"
          }
        }
      ]
  })
}

#CoRise TODO: create metric alters
resource "aws_cloudwatch_metric_alarm" "bot_attack" {
  alarm_name          = "bot_attack"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "$auth/register_visitor_count"
  namespace           = "flaskbb_app"
  period              = 60
  statistic           = "Sum"
  threshold           = 10
  alarm_description   = "The bots area attacking our forum, help us Neo!"
}

resource "aws_cloudwatch_metric_alarm" "too_busy" {
  alarm_name          = "too_busy"
  comparison_operator = "LessThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "CPUIdle"
  namespace           = "AWS/ElasticBeanstalk"
  period              = 300
  statistic           = "Average"
  alarm_description   = "Hey, I'd doing real work here, what give! I need a break!"
}