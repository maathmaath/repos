while read i; do
	echo $i
	curl 'https://stageapp.tekioncloud.xyz/api/printer-mgmt/u/printer/ip-addresses' \
  	-H 'authority: stageapp.tekioncloud.xyz' \
  	-H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
  	-H 'tek-siteid: -1_4' \
  	-H 'tenantname: stg-cacargroup' \
  	-H 'clientid: web' \
  	-H 'userid: 32b87bf1-1361-4c29-953f-871580c4b36d' \
  	-H 'roleid: 4_SuperAdmin' \
  	-H 'traceparent: 00-6d36bba2e3862573b5d8b1715fbc17bc-8edae5acf66e1fa6-01' \
  	-H 'sec-ch-ua-mobile: ?0' \
  	-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
  	-H 'tekion-api-token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6ImdhdXJhdnByaW50aW5nIiwibmFtZSI6ImdhdXJhdnByaW50aW5nQG1haWxpbmF0b3IuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzJiMTZmMzNiYjY1YjNjYzZmOTc1MjI2MDlmMjk0ZDgyP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZ2EucG5nIiwidXBkYXRlZF9hdCI6IjIwMjEtMDgtMzFUMDU6NDE6MDIuODM0WiIsImVtYWlsIjoiZ2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly90ZWtpb24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzUwMmQ5NmIzYTYzMDA2OGE4OGYyOCIsImF1ZCI6ImxNU3pxYlM3OEVua1hwNXJoWTdaZFZkZHMwQVh2QzRSIiwiaWF0IjoxNjMwMzg4NDYzLCJleHAiOjE2MzA0MjQ0NjN9.ZSp-jz7Ncvy2dTiNixyZnik3nGMlcog17mvQkRH3PK5OOMWSH6qI30W98e4Mnb86Cp-_YREeDlVjiiLGqmbtmKj3MDq1G6j0b3JKpWhfbojQXPgJ5Q46uy5N92QL40q_v-5E_po6IaqCDU9sX10N5g2o38GM6tnmHcn1fR5NanWke4ohFG9JW0b1lHeslDBvqfb-dAMcv3p8BSY6-ltO9lR4S4k7LB3QhXOgVWqnLgIpXAjr-PPWc38M9hNlhJcNzLX873WLLGzqfBEbmb4vWtHx65y-dnnRZNISC8W5QcFKFt_38dRF-LYM8uWjlBZGQVoukSgC6EJNdRxK787vmg' \
  	-H 'tenantid: undefined' \
  	-H 'content-type: application/json' \
  	-H 'accept: application/json, text/plain, */*' \
  	-H 'original-userid: null' \
  	-H 'dealerid: 4' \
  	-H 'original-tenantid: null' \
  	-H 'origin: https://stageapp.tekioncloud.xyz' \
  	-H 'sec-fetch-site: same-origin' \
  	-H 'sec-fetch-mode: cors' \
  	-H 'sec-fetch-dest: empty' \
  	-H 'referer: https://stageapp.tekioncloud.xyz/internal/printer-management/add-printer' \
  	-H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
  	-H 'cookie: deviceId=d0d1bca3-872a-400f-87ae-a848d8401734; redirected_from=https://stageapp.tekioncloud.xyz/internal/printer-management; tcookie={%22tekion-api-token%22:%22eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6ImdhdXJhdnByaW50aW5nIiwibmFtZSI6ImdhdXJhdnByaW50aW5nQG1haWxpbmF0b3IuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzJiMTZmMzNiYjY1YjNjYzZmOTc1MjI2MDlmMjk0ZDgyP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZ2EucG5nIiwidXBkYXRlZF9hdCI6IjIwMjEtMDgtMzFUMDU6NDE6MDIuODM0WiIsImVtYWlsIjoiZ2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly90ZWtpb24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzUwMmQ5NmIzYTYzMDA2OGE4OGYyOCIsImF1ZCI6ImxNU3pxYlM3OEVua1hwNXJoWTdaZFZkZHMwQVh2QzRSIiwiaWF0IjoxNjMwMzg4NDYzLCJleHAiOjE2MzA0MjQ0NjN9.ZSp-jz7Ncvy2dTiNixyZnik3nGMlcog17mvQkRH3PK5OOMWSH6qI30W98e4Mnb86Cp-_YREeDlVjiiLGqmbtmKj3MDq1G6j0b3JKpWhfbojQXPgJ5Q46uy5N92QL40q_v-5E_po6IaqCDU9sX10N5g2o38GM6tnmHcn1fR5NanWke4ohFG9JW0b1lHeslDBvqfb-dAMcv3p8BSY6-ltO9lR4S4k7LB3QhXOgVWqnLgIpXAjr-PPWc38M9hNlhJcNzLX873WLLGzqfBEbmb4vWtHx65y-dnnRZNISC8W5QcFKFt_38dRF-LYM8uWjlBZGQVoukSgC6EJNdRxK787vmg%22%2C%22roleId%22:%224_SuperAdmin%22%2C%22userId%22:%2232b87bf1-1361-4c29-953f-871580c4b36d%22%2C%22tenantname%22:%22stg-cacargroup%22%2C%22dealerId%22:%224%22%2C%22original-userid%22:null%2C%22original-tenantid%22:null%2C%22clientId%22:%22web%22%2C%22tek-siteId%22:%22-1_4%22}' \
  	--data-raw '["$i"]' \
  	--compressed
done<ips.txt
