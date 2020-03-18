unit VSM.Rest.Enumeradores;

interface
  type
   TVSMRestTipoAutenticacao = (tpNoAuth,
                              tpApiKey,
                              tpBearerToken,
                              tpBasicAuth,
                              tpDigestAuth,
                              tpOAuth1,
                              tpOAuth2,
                              tpHawkAuthentication,
                              tpAWSSignature,
                              tpNTLMAuthentication,
                              tpAkamaiEdgeGrid
                              );

//   0-NoAuth, 1-ApiKey, 2-BearerToken, 3-BasicAuth, 4-DigestAuth,
//   5-OAuth1, 6-OAuth2, 7-HawkAuthentication, 8-AWSSignature, 9-NTLMAuthentication, 10-AkamaiEdgeGrid

implementation

end.
