export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type MakeEmpty<T extends { [key: string]: unknown }, K extends keyof T> = { [_ in K]?: never };
export type Incremental<T> = T | { [P in keyof T]?: P extends ' $fragmentName' | '__typename' ? T[P] : never };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: { input: string; output: string; }
  String: { input: string; output: string; }
  Boolean: { input: boolean; output: boolean; }
  Int: { input: number; output: number; }
  Float: { input: number; output: number; }
};

export type AiHubVoiceModel = {
  __typename?: 'AIHubVoiceModel';
  backupUrls: AiHubVoiceModelBackupUrlsConnection;
  checksumMD5ForWeights: Scalars['String']['output'];
  creatorText?: Maybe<Scalars['String']['output']>;
  derivedModel?: Maybe<VoiceModel>;
  derivedModelId?: Maybe<Scalars['ID']['output']>;
  downloadCount: Scalars['Int']['output'];
  filename: Scalars['String']['output'];
  id: Scalars['ID']['output'];
  inferredProfile?: Maybe<VoiceModelProfile>;
  name?: Maybe<Scalars['String']['output']>;
  version: Scalars['String']['output'];
};


export type AiHubVoiceModelBackupUrlsArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
};

export type AiHubVoiceModelBackupUrlsConnection = {
  __typename?: 'AIHubVoiceModelBackupUrlsConnection';
  edges: Array<Maybe<AiHubVoiceModelBackupUrlsEdge>>;
  pageInfo: PageInfo;
};

export type AiHubVoiceModelBackupUrlsEdge = {
  __typename?: 'AIHubVoiceModelBackupUrlsEdge';
  cursor: Scalars['String']['output'];
  node: VoiceModelBackupUrl;
};

export type AiHubVoiceModelsConnection = {
  __typename?: 'AIHubVoiceModelsConnection';
  edges: Array<Maybe<AiHubVoiceModelsEdge>>;
  pageInfo: PageInfo;
};

export type AiHubVoiceModelsEdge = {
  __typename?: 'AIHubVoiceModelsEdge';
  cursor: Scalars['String']['output'];
  node: AiHubVoiceModel;
};

export type CreateAiHubVoiceModelInput = {
  checksumMD5ForWeights: Scalars['String']['input'];
  creatorText?: InputMaybe<Scalars['String']['input']>;
  derivedModelId?: InputMaybe<Scalars['ID']['input']>;
  downloadCount: Scalars['Int']['input'];
  filename: Scalars['String']['input'];
  name?: InputMaybe<Scalars['String']['input']>;
  version: Scalars['String']['input'];
};

export type CreateTextToSpeechInput = {
  inputText: Scalars['String']['input'];
  ouputUrl: Scalars['String']['input'];
  voiceModelId: Scalars['ID']['input'];
};

export type CreateVoiceModelBackupUrlInput = {
  url: Scalars['String']['input'];
  voiceModelId: Scalars['ID']['input'];
};

export type CreateVoiceModelConfigInput = {
  artifactProtection: Scalars['Float']['input'];
  audioResampling: Scalars['Int']['input'];
  f0Curve: Scalars['String']['input'];
  filterRadius: Scalars['Int']['input'];
  pitchExtractionMethod: Scalars['String']['input'];
  qualityScore: Scalars['Float']['input'];
  searchFeatureRatio: Scalars['Float']['input'];
  transposePitch: Scalars['Int']['input'];
  voiceModelId: Scalars['ID']['input'];
  volumeEnvelopeScaling: Scalars['Float']['input'];
};

export type CreateVoiceModelInput = {
  checksumMD5ForAdded: Scalars['String']['input'];
  checksumMD5ForWeights: Scalars['String']['input'];
  checksumSHA256ForAdded: Scalars['String']['input'];
  checksumSHA256ForWeights: Scalars['String']['input'];
  filesizeForAdded: Scalars['Int']['input'];
  filesizeForWeights: Scalars['Int']['input'];
  hidden: Scalars['Boolean']['input'];
  name: Scalars['String']['input'];
  processed: Scalars['Boolean']['input'];
};

export type CreateVoiceModelProfileInput = {
  accent: Scalars['String']['input'];
  confidence: Scalars['Float']['input'];
  fictional: Scalars['Boolean']['input'];
  gender: Scalars['String']['input'];
  modelTrainedOnEnglishProbability: Scalars['Float']['input'];
  name: Scalars['String']['input'];
  nativeLanguage: Scalars['String']['input'];
  relevantTags: Array<Scalars['String']['input']>;
  voiceModelId: Scalars['ID']['input'];
};

export type Mutation = {
  __typename?: 'Mutation';
  createAIHubVoiceModel: AiHubVoiceModel;
  createTextToSpeech: TextToSpeech;
  createVoiceModel: VoiceModel;
  createVoiceModelBackupUrl: VoiceModelBackupUrl;
  createVoiceModelConfig: VoiceModelConfig;
  createVoiceModelProfile: VoiceModelProfile;
  updateAIHubVoiceModel: AiHubVoiceModel;
  updateTextToSpeech: TextToSpeech;
  updateVoiceModel: VoiceModel;
  updateVoiceModelBackupUrl: VoiceModelBackupUrl;
  updateVoiceModelConfig: VoiceModelConfig;
  updateVoiceModelProfile: VoiceModelProfile;
};


export type MutationCreateAiHubVoiceModelArgs = {
  input: CreateAiHubVoiceModelInput;
};


export type MutationCreateTextToSpeechArgs = {
  input: CreateTextToSpeechInput;
};


export type MutationCreateVoiceModelArgs = {
  input: CreateVoiceModelInput;
};


export type MutationCreateVoiceModelBackupUrlArgs = {
  input: CreateVoiceModelBackupUrlInput;
};


export type MutationCreateVoiceModelConfigArgs = {
  input: CreateVoiceModelConfigInput;
};


export type MutationCreateVoiceModelProfileArgs = {
  input: CreateVoiceModelProfileInput;
};


export type MutationUpdateAiHubVoiceModelArgs = {
  input: UpdateAiHubVoiceModelInput;
};


export type MutationUpdateTextToSpeechArgs = {
  input: UpdateTextToSpeechInput;
};


export type MutationUpdateVoiceModelArgs = {
  input: UpdateVoiceModelInput;
};


export type MutationUpdateVoiceModelBackupUrlArgs = {
  input: UpdateVoiceModelBackupUrlInput;
};


export type MutationUpdateVoiceModelConfigArgs = {
  input: UpdateVoiceModelConfigInput;
};


export type MutationUpdateVoiceModelProfileArgs = {
  input: UpdateVoiceModelProfileInput;
};

export type PageInfo = {
  __typename?: 'PageInfo';
  endCursor?: Maybe<Scalars['String']['output']>;
  hasNextPage: Scalars['Boolean']['output'];
  hasPreviousPage: Scalars['Boolean']['output'];
  startCursor?: Maybe<Scalars['String']['output']>;
};

export type Query = {
  __typename?: 'Query';
  AIHubVoiceModel: AiHubVoiceModel;
  AIHubVoiceModels: AiHubVoiceModelsConnection;
  TextToSpeech: TextToSpeech;
  TextToSpeeches: TextToSpeechesConnection;
  VoiceModel: VoiceModel;
  VoiceModelBackupUrl: VoiceModelBackupUrl;
  VoiceModelBackupUrls: VoiceModelBackupUrlsConnection;
  VoiceModelConfig: VoiceModelConfig;
  VoiceModelConfigs: VoiceModelConfigsConnection;
  VoiceModelProfile: VoiceModelProfile;
  VoiceModelProfiles: VoiceModelProfilesConnection;
  VoiceModels: VoiceModelsConnection;
};


export type QueryAiHubVoiceModelArgs = {
  checksumMD5ForWeights?: InputMaybe<Scalars['String']['input']>;
  id?: InputMaybe<Scalars['ID']['input']>;
};


export type QueryAiHubVoiceModelsArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
  minDownloadCount?: InputMaybe<Scalars['Int']['input']>;
};


export type QueryTextToSpeechArgs = {
  id: Scalars['ID']['input'];
};


export type QueryTextToSpeechesArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
};


export type QueryVoiceModelArgs = {
  id: Scalars['ID']['input'];
};


export type QueryVoiceModelBackupUrlArgs = {
  id: Scalars['ID']['input'];
};


export type QueryVoiceModelBackupUrlsArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
};


export type QueryVoiceModelConfigArgs = {
  id: Scalars['ID']['input'];
};


export type QueryVoiceModelConfigsArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
};


export type QueryVoiceModelProfileArgs = {
  id: Scalars['ID']['input'];
};


export type QueryVoiceModelProfilesArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
};


export type QueryVoiceModelsArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
};

export type TextToSpeech = {
  __typename?: 'TextToSpeech';
  id: Scalars['ID']['output'];
  inputText: Scalars['String']['output'];
  ouputUrl: Scalars['String']['output'];
  voiceModel: VoiceModel;
  voiceModelId: Scalars['ID']['output'];
};

export type TextToSpeechesConnection = {
  __typename?: 'TextToSpeechesConnection';
  edges: Array<Maybe<TextToSpeechesEdge>>;
  pageInfo: PageInfo;
};

export type TextToSpeechesEdge = {
  __typename?: 'TextToSpeechesEdge';
  cursor: Scalars['String']['output'];
  node: TextToSpeech;
};

export type UpdateAiHubVoiceModelInput = {
  checksumMD5ForWeights?: InputMaybe<Scalars['String']['input']>;
  creatorText?: InputMaybe<Scalars['String']['input']>;
  derivedModelId?: InputMaybe<Scalars['ID']['input']>;
  downloadCount?: InputMaybe<Scalars['Int']['input']>;
  filename?: InputMaybe<Scalars['String']['input']>;
  id: Scalars['ID']['input'];
  name?: InputMaybe<Scalars['String']['input']>;
  version?: InputMaybe<Scalars['String']['input']>;
};

export type UpdateTextToSpeechInput = {
  id: Scalars['ID']['input'];
  inputText?: InputMaybe<Scalars['String']['input']>;
  ouputUrl?: InputMaybe<Scalars['String']['input']>;
  voiceModelId?: InputMaybe<Scalars['ID']['input']>;
};

export type UpdateVoiceModelBackupUrlInput = {
  id: Scalars['ID']['input'];
  url?: InputMaybe<Scalars['String']['input']>;
  voiceModelId?: InputMaybe<Scalars['ID']['input']>;
};

export type UpdateVoiceModelConfigInput = {
  artifactProtection?: InputMaybe<Scalars['Float']['input']>;
  audioResampling?: InputMaybe<Scalars['Int']['input']>;
  f0Curve?: InputMaybe<Scalars['String']['input']>;
  filterRadius?: InputMaybe<Scalars['Int']['input']>;
  id: Scalars['ID']['input'];
  pitchExtractionMethod?: InputMaybe<Scalars['String']['input']>;
  qualityScore?: InputMaybe<Scalars['Float']['input']>;
  searchFeatureRatio?: InputMaybe<Scalars['Float']['input']>;
  transposePitch?: InputMaybe<Scalars['Int']['input']>;
  voiceModelId?: InputMaybe<Scalars['ID']['input']>;
  volumeEnvelopeScaling?: InputMaybe<Scalars['Float']['input']>;
};

export type UpdateVoiceModelInput = {
  checksumMD5ForAdded?: InputMaybe<Scalars['String']['input']>;
  checksumMD5ForWeights?: InputMaybe<Scalars['String']['input']>;
  checksumSHA256ForAdded?: InputMaybe<Scalars['String']['input']>;
  checksumSHA256ForWeights?: InputMaybe<Scalars['String']['input']>;
  filesizeForAdded?: InputMaybe<Scalars['Int']['input']>;
  filesizeForWeights?: InputMaybe<Scalars['Int']['input']>;
  hidden?: InputMaybe<Scalars['Boolean']['input']>;
  id: Scalars['ID']['input'];
  name?: InputMaybe<Scalars['String']['input']>;
  processed?: InputMaybe<Scalars['Boolean']['input']>;
};

export type UpdateVoiceModelProfileInput = {
  accent?: InputMaybe<Scalars['String']['input']>;
  confidence?: InputMaybe<Scalars['Float']['input']>;
  fictional?: InputMaybe<Scalars['Boolean']['input']>;
  gender?: InputMaybe<Scalars['String']['input']>;
  id: Scalars['ID']['input'];
  modelTrainedOnEnglishProbability?: InputMaybe<Scalars['Float']['input']>;
  name?: InputMaybe<Scalars['String']['input']>;
  nativeLanguage?: InputMaybe<Scalars['String']['input']>;
  relevantTags?: InputMaybe<Array<Scalars['String']['input']>>;
  voiceModelId?: InputMaybe<Scalars['ID']['input']>;
};

export type VoiceModel = {
  __typename?: 'VoiceModel';
  checksumMD5ForAdded: Scalars['String']['output'];
  checksumMD5ForWeights: Scalars['String']['output'];
  checksumSHA256ForAdded: Scalars['String']['output'];
  checksumSHA256ForWeights: Scalars['String']['output'];
  filesizeForAdded: Scalars['Int']['output'];
  filesizeForWeights: Scalars['Int']['output'];
  hidden: Scalars['Boolean']['output'];
  id: Scalars['ID']['output'];
  modelConfig?: Maybe<VoiceModelConfig>;
  name: Scalars['String']['output'];
  processed: Scalars['Boolean']['output'];
  sourceModel?: Maybe<AiHubVoiceModel>;
  textToSpeeches: VoiceModelTextToSpeechesConnection;
};


export type VoiceModelTextToSpeechesArgs = {
  after?: InputMaybe<Scalars['String']['input']>;
  before?: InputMaybe<Scalars['String']['input']>;
  first?: InputMaybe<Scalars['Int']['input']>;
  last?: InputMaybe<Scalars['Int']['input']>;
};

export type VoiceModelBackupUrl = {
  __typename?: 'VoiceModelBackupUrl';
  id: Scalars['ID']['output'];
  url: Scalars['String']['output'];
  voiceModel: AiHubVoiceModel;
  voiceModelId: Scalars['ID']['output'];
};

export type VoiceModelBackupUrlsConnection = {
  __typename?: 'VoiceModelBackupUrlsConnection';
  edges: Array<Maybe<VoiceModelBackupUrlsEdge>>;
  pageInfo: PageInfo;
};

export type VoiceModelBackupUrlsEdge = {
  __typename?: 'VoiceModelBackupUrlsEdge';
  cursor: Scalars['String']['output'];
  node: VoiceModelBackupUrl;
};

export type VoiceModelConfig = {
  __typename?: 'VoiceModelConfig';
  artifactProtection: Scalars['Float']['output'];
  audioResampling: Scalars['Int']['output'];
  f0Curve: Scalars['String']['output'];
  filterRadius: Scalars['Int']['output'];
  id: Scalars['ID']['output'];
  pitchExtractionMethod: Scalars['String']['output'];
  qualityScore: Scalars['Float']['output'];
  searchFeatureRatio: Scalars['Float']['output'];
  transposePitch: Scalars['Int']['output'];
  voiceModel: VoiceModel;
  voiceModelId: Scalars['ID']['output'];
  volumeEnvelopeScaling: Scalars['Float']['output'];
};

export type VoiceModelConfigsConnection = {
  __typename?: 'VoiceModelConfigsConnection';
  edges: Array<Maybe<VoiceModelConfigsEdge>>;
  pageInfo: PageInfo;
};

export type VoiceModelConfigsEdge = {
  __typename?: 'VoiceModelConfigsEdge';
  cursor: Scalars['String']['output'];
  node: VoiceModelConfig;
};

export type VoiceModelProfile = {
  __typename?: 'VoiceModelProfile';
  accent: Scalars['String']['output'];
  confidence: Scalars['Float']['output'];
  fictional: Scalars['Boolean']['output'];
  gender: Scalars['String']['output'];
  id: Scalars['ID']['output'];
  modelTrainedOnEnglishProbability: Scalars['Float']['output'];
  name: Scalars['String']['output'];
  nativeLanguage: Scalars['String']['output'];
  relevantTags: Array<Scalars['String']['output']>;
  voiceModel: AiHubVoiceModel;
  voiceModelId: Scalars['ID']['output'];
};

export type VoiceModelProfilesConnection = {
  __typename?: 'VoiceModelProfilesConnection';
  edges: Array<Maybe<VoiceModelProfilesEdge>>;
  pageInfo: PageInfo;
};

export type VoiceModelProfilesEdge = {
  __typename?: 'VoiceModelProfilesEdge';
  cursor: Scalars['String']['output'];
  node: VoiceModelProfile;
};

export type VoiceModelTextToSpeechesConnection = {
  __typename?: 'VoiceModelTextToSpeechesConnection';
  edges: Array<Maybe<VoiceModelTextToSpeechesEdge>>;
  pageInfo: PageInfo;
};

export type VoiceModelTextToSpeechesEdge = {
  __typename?: 'VoiceModelTextToSpeechesEdge';
  cursor: Scalars['String']['output'];
  node: TextToSpeech;
};

export type VoiceModelsConnection = {
  __typename?: 'VoiceModelsConnection';
  edges: Array<Maybe<VoiceModelsEdge>>;
  pageInfo: PageInfo;
};

export type VoiceModelsEdge = {
  __typename?: 'VoiceModelsEdge';
  cursor: Scalars['String']['output'];
  node: VoiceModel;
};

export type AiHubVoiceModelsQueryVariables = Exact<{
  after?: InputMaybe<Scalars['String']['input']>;
}>;


export type AiHubVoiceModelsQuery = { __typename?: 'Query', AIHubVoiceModels: { __typename?: 'AIHubVoiceModelsConnection', pageInfo: { __typename?: 'PageInfo', endCursor?: string | null, hasNextPage: boolean, hasPreviousPage: boolean, startCursor?: string | null }, edges: Array<{ __typename?: 'AIHubVoiceModelsEdge', node: { __typename?: 'AIHubVoiceModel', downloadCount: number, filename: string, name?: string | null, checksumMD5ForWeights: string, inferredProfile?: { __typename?: 'VoiceModelProfile', accent: string, confidence: number, fictional: boolean, gender: string, id: string, modelTrainedOnEnglishProbability: number, name: string, nativeLanguage: string, relevantTags: Array<string>, voiceModelId: string } | null, backupUrls: { __typename?: 'AIHubVoiceModelBackupUrlsConnection', edges: Array<{ __typename?: 'AIHubVoiceModelBackupUrlsEdge', node: { __typename?: 'VoiceModelBackupUrl', id: string, url: string, voiceModelId: string } } | null> } } } | null> } };
