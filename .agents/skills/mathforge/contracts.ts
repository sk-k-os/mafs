// Design contracts only. No runtime adapter or validator is implemented here.
export type ArtifactHash = string;
export type ClaimId = string;
export type JsonValue = null | boolean | number | string | JsonValue[] | { [key: string]: JsonValue };
export interface ArtifactRef {
  uri: string;
  sha256: ArtifactHash;
  byteLength: number;
  mediaType: string;
  revision: string;
  sourceTrust: "externalData" | "generatedCandidate" | "trustedReceipt" | "humanDecision";
}
export interface ClaimRef { id: ClaimId; revision: string; statementHash: ArtifactHash }
export interface Dependency { premise: ClaimRef; use: "logicalPremise" | "heuristicInspiration"; assumption: boolean }
export interface MathematicalClaim {
  identity: ClaimRef;
  informalStatement: ArtifactRef;
  formalStatement: ArtifactRef | null;
  definitions: ArtifactRef[];
  explicitAssumptions: ArtifactRef[];
  dependencies: Dependency[];
  epistemicClass: "speculation" | "numericalEvidence" | "conditionalTheorem" | "mathematicalArgument";
  disposition: "candidate" | "underReview" | "acceptedAtRecordedAssurance" | "refuted" | "stale" | "retracted";
  formalization: "notAttempted" | "partial" | "checkedUnderRecordedTrust" | "failed";
  expertReview: "unreviewed" | "acceptedUnderStatedAssumptions" | "rejected" | "inconclusive";
  novelty: "notAssessed" | "known" | "potentiallyNew" | "expertAssessed";
  relevance: { targetObligation: ClaimRef; proposedBridge: ArtifactRef; review: ArtifactRef | null };
  evidence: ArtifactRef[];
  unresolvedObjections: ArtifactRef[];
  authorInstanceId: string;
  acceptanceReceipt: ArtifactRef | null;
}
export interface Budget {
  maxWallSeconds: number;
  maxWorkerSeconds: number;
  maxTokens: number | null;
  maxCurrencyUnits: number | null;
  currency: string | null;
  reservedCurrencyUnits: number;
  consumedCurrencyUnits: number;
  priceSchedule: ArtifactRef | null;
}
export interface Assignment {
  id: string;
  revision: string;
  parentId: string | null;
  campaignId: string;
  objective: string;
  phase: "design" | "calibration" | "research" | "verification";
  exactTarget: ClaimRef;
  inputArtifacts: ArtifactRef[];
  consumedContextRevision: string;
  roleDefinitionRevision: string;
  allowedCapabilities: string[];
  writablePaths: string[];
  dependencies: ClaimRef[];
  acceptanceCases: string[];
  experimentRequired: boolean;
  formalVerificationRequired: boolean;
  requiredCheckIds: string[];
  budget: Budget;
  deadline: string;
  idempotencyKey: string;
  requiredDecision: ArtifactRef | null;
}
export interface AgentDefinition {
  id: string;
  revision: string;
  responsibility: string;
  thinkingMode: string;
  requiredSources: ArtifactRef[];
  toolBindings: string[];
  outputSchema: ArtifactRef;
  admissionSuite: ArtifactRef;
  authorityPolicy: ArtifactRef;
}
export interface AgentInstance {
  id: string;
  definition: AgentDefinition;
  parentInstanceId: string | null;
  depth: number;
  status: "quarantined" | "calibrating" | "ready" | "working" | "held" | "retiring" | "retired";
  modelBinding: { provider: string; model: string; revision: string | null };
  predecessorId: string | null;
  handoff: ArtifactRef | null;
  admissionReceipt: ArtifactRef | null;
  assignments: string[];
}
export interface FormalVerificationReceipt {
  claim: ClaimRef;
  sourceTree: ArtifactRef;
  immutableTarget: ArtifactRef;
  toolchain: ArtifactRef;
  buildExitCode: number;
  buildLogs: ArtifactRef;
  elaboratedStatement: ArtifactRef;
  statementComparison: "equal" | "different" | "inconclusive";
  transitiveAxioms: string[];
  approvedAxiomPolicy: ArtifactRef;
  proofReplay: ArtifactRef | null;
  externalChecker: ArtifactRef | null;
  semanticReview: ArtifactRef | null;
  verdict: "acceptedUnderRecordedTrust" | "rejected" | "inconclusive";
  signer: "trustedVerificationService";
}
export interface HumanDecision {
  checkpointId: string;
  checkpointRevision: string;
  reviewedArtifacts: ArtifactRef[];
  reviewerIdentity: string;
  reviewerRole: "programOwner" | "mathematicalDirector" | "independentExpert";
  originalResponse: ArtifactRef;
  disposition: "accept" | "revise" | "stop" | "clarify";
  interpretedScope: string;
  authenticatedAt: string;
  appliedTransitionReceipt: ArtifactRef | null;
}
export interface PayloadRef {
  artifact: ArtifactRef | null;
  representation: "rawProviderRequest" | "rawProviderResponse" | "validatedToolInput" | "rawToolResult" | "parsedOutput";
  captureState: "available" | "pending" | "redacted" | "truncated" | "notCaptured" | "expired" | "denied";
}
export interface RunEvent {
  eventId: string;
  schemaVersion: string;
  campaignId: string;
  workflowVersion: string;
  assignmentId: string;
  activationId: string;
  attemptId: string;
  instanceId: string;
  cursor: number;
  stateRevision: number;
  causedBy: string[];
  occurredAt: string;
  receivedAt: string;
  type: "queued" | "started" | "waiting" | "completed" | "failed" | "retried" | "skipped" | "canceled" | "checkpoint" | "resumed" | "invalidated";
  input: PayloadRef | null;
  output: PayloadRef | null;
  error: ArtifactRef | null;
}
export interface ToolResult {
  requestId: string;
  status: "completed" | "rejected" | "unavailable" | "inconclusive";
  artifacts: ArtifactRef[];
  actualEffects: string[];
  assumptionLedger: ArtifactRef | null;
  resourceReceipt: ArtifactRef;
  errorCode: string | null;
}
export interface SourceFetchInput { url: string; expectedVersion: string | null; permittedDestination: string }
export interface ComputeInput { program: ArtifactRef; inputs: ArtifactRef[]; imageDigest: string; limit: Budget; proofSettings: JsonValue }
export interface VerifyInput { claim: ClaimRef; proof: ArtifactRef; challenge: ArtifactRef; toolchain: ArtifactRef }
export interface SpawnProposal { definition: AgentDefinition; assignment: Assignment; capabilityGapEvidence: ArtifactRef }
export interface ProposedAdapters {
  fetchSource(input: SourceFetchInput): Promise<ToolResult>;
  runIsolatedComputation(input: ComputeInput): Promise<ToolResult>;
  verifyFormalProof(input: VerifyInput): Promise<FormalVerificationReceipt>;
  proposeSpecialist(input: SpawnProposal): Promise<ToolResult>;
  submitCandidate(input: MathematicalClaim): Promise<ToolResult>;
  recordHumanDecision(input: HumanDecision): Promise<ToolResult>;
}

// Normalized design records, not copies of provider wire schemas.
// Generate and pin actual app server types from the selected CLI at implementation.
export type AccountSlotId = "01" | "02" | "03" | "04" | "05" | "06";
export interface AccountBinding {
  slotId: AccountSlotId;
  protectedAccountRef: string;
  connectionGeneration: string;
  actualAuthType: "chatgpt";
  authenticatedPlan: string | null;
  identityReceipt: ArtifactRef;
  privateHomeBindingReceipt: ArtifactRef;
  isolationQualification: ArtifactRef;
  availableModelsReceipt: ArtifactRef;
  status: "enrolling" | "ready" | "held" | "disconnected";
  holdReason: string | null;
}
export interface UsageWindowObservation {
  usedPercent: number | null;
  windowDurationMinutes: number | null;
  resetsAtUnixSeconds: number | null;
}
export interface UsageBucketObservation {
  // A bucket ID is scoped to an account observation, not a global pool ID.
  meteredLimitId: string | null;
  primary: UsageWindowObservation | null;
  secondary: UsageWindowObservation | null;
  creditsPresent: boolean | null;
  spendControlReached: boolean | null;
  rawReceipt: ArtifactRef;
}
export interface AccountUsageObservation {
  protectedAccountRef: string;
  connectionGeneration: string;
  observedAt: string;
  freshnessPolicyRevision: string;
  providerAccountIdentityReceipt: ArtifactRef | null;
  identityReconciliation: "matched" | "conflicting" | "unavailable";
  ordinaryUsageAllowed: boolean | null;
  buckets: UsageBucketObservation[];
  evidence: ArtifactRef;
}
export type PoolRelationship = {
  status: "unknown";
  protectedAccountRefs: string[];
} | {
  status: "verifiedShared" | "verifiedIndependent";
  protectedAccountRefs: string[];
  poolRefs: string[];
  evidence: ArtifactRef;
  effectiveAt: string;
};
export interface IncludedUsageBoundary {
  protectedAccountRef: string;
  policyRevision: string;
  state: "unverified" | "verified" | "failed" | "stale";
  evidence: ArtifactRef | null;
  validUntil: string | null;
  additionalSpendAuthorized: false;
  apiFallbackAllowed: false;
  creditPurchaseAllowed: false;
}
export interface AccountDispatchPermit {
  permitId: string;
  assignmentId: string;
  assignmentRevision: string;
  attemptId: string;
  instanceId: string;
  slotId: AccountSlotId;
  protectedAccountRef: string;
  connectionGeneration: string;
  modelBindingReceipt: ArtifactRef;
  usageObservation: ArtifactRef;
  includedUsageBoundary: ArtifactRef;
  inputManifest: ArtifactRef;
  capabilityPolicy: ArtifactRef;
  leaseRevision: number;
  reservedBudget: Budget;
  expiresAt: string;
  issuer: "trustedBroker";
  signatureReceipt: ArtifactRef;
}
export interface BrokerEnvelope {
  messageId: string;
  campaignId: string;
  assignmentId: string;
  assignmentRevision: string;
  authenticatedSenderInstanceId: string;
  recipientRoleId: string;
  claim: ClaimRef | null;
  artifacts: ArtifactRef[];
  requestedAction: "analyze" | "experiment" | "review" | "respondToObjection" | "prepareHandoff" | "proposeSpecialist";
  visibility: "discoveryBranch" | "blindReview" | "postReviewDialogue" | "evaluation";
  inputManifest: ArtifactRef;
  deadline: string;
  idempotencyKey: string;
  brokerReceipt: ArtifactRef;
}
export interface ReviewExposureRecord {
  claim: ClaimRef;
  reviewerInstanceId: string;
  contributionHistory: ArtifactRef;
  admittedInputManifest: ArtifactRef;
  priorVerdictExposure: "excluded" | "exposed" | "unknown";
  independenceAssessment: "admittedWithRecordedLimits" | "disqualified" | "inconclusive";
  initialReviewCommitment: ArtifactRef | null;
  subsequentDialogue: ArtifactRef[];
}
export interface ModelUsageAttribution {
  attemptId: string;
  slotId: AccountSlotId;
  protectedAccountRef: string;
  connectionGeneration: string;
  providerRequestReceipt: ArtifactRef | null;
  outcome: "completed" | "failed" | "canceled" | "unknown";
  workerSeconds: number | null;
  providerReportedTokens: number | null;
  measuredAdditionalCost: number | null;
  costCurrency: string | null;
  consumptionUncertain: boolean;
  reconciliationHistory: ArtifactRef[];
}
